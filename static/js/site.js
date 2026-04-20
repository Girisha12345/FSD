function getCookie(name) {
    const cookieValue = document.cookie
        .split('; ')
        .find((row) => row.startsWith(`${name}=`));
    return cookieValue ? decodeURIComponent(cookieValue.split('=')[1]) : null;
}

function setFormMessage(message, type = 'danger') {
    const formMessage = document.getElementById('formMessage');
    if (!formMessage) {
        return;
    }

    formMessage.className = `small mb-2 text-${type}`;
    formMessage.textContent = message;
}

function validateInquiryPayload(payload) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const onlyDigits = payload.phone.replace(/\D/g, '');

    if (!payload.student_name) {
        return 'Student name is required.';
    }

    if (!emailRegex.test(payload.email)) {
        return 'Enter a valid email address.';
    }

    if (onlyDigits.length !== 10) {
        return 'Phone number must contain exactly 10 digits.';
    }

    if (!Number.isInteger(payload.course)) {
        return 'Please select a course.';
    }

    if (!payload.consent) {
        return 'Consent is required to register an inquiry.';
    }

    return null;
}

async function loadCoursesForDropdown(selectElement) {
    try {
        const response = await fetch('/api/courses/');
        if (!response.ok) {
            throw new Error('Failed to fetch courses');
        }

        const courses = await response.json();
        courses.forEach((course) => {
            const option = document.createElement('option');
            option.value = course.id;
            option.textContent = `${course.course_name} - ${course.specialization}`;
            selectElement.appendChild(option);
        });
    } catch (error) {
        console.error(error);
    }
}

async function submitInquiryForm(form, inquiryModalInstance) {
    const submitButton = form.querySelector('button[type="submit"]');
    const payload = {
        student_name: form.student_name.value.trim(),
        email: form.email.value.trim(),
        phone: form.phone.value.trim(),
        course: parseInt(form.course.value, 10),
        consent: form.consent.checked,
    };

    const validationError = validateInquiryPayload(payload);
    if (validationError) {
        setFormMessage(validationError, 'danger');
        return;
    }

    if (submitButton) {
        submitButton.disabled = true;
    }

    setFormMessage('Submitting inquiry...', 'secondary');

    try {
        const response = await fetch('/api/register/', {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') || document.querySelector('[name=csrfmiddlewaretoken]')?.value || '',
            },
            body: JSON.stringify(payload),
        });

        const raw = await response.text();
        const data = raw ? JSON.parse(raw) : {};

        if (!response.ok) {
            const firstError = Object.values(data)[0];
            const message = Array.isArray(firstError)
                ? firstError[0]
                : firstError || 'Unable to submit inquiry. Please try again.';
            setFormMessage(message, 'danger');
            return;
        }

        form.reset();
        setFormMessage(data.message || 'Inquiry submitted successfully', 'success');

        window.setTimeout(() => {
            if (inquiryModalInstance) {
                inquiryModalInstance.hide();
            }
        }, 900);
    } catch (error) {
        setFormMessage('Unable to submit inquiry. Please try again.', 'danger');
    } finally {
        if (submitButton) {
            submitButton.disabled = false;
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const shouldOpenModal = document.body.dataset.openRegistrationModal === 'true';
    const inquiryModalElement = document.getElementById('inquiryModal');
    const inquiryModalInstance = inquiryModalElement ? new bootstrap.Modal(inquiryModalElement) : null;

    if (shouldOpenModal && inquiryModalInstance) {
        inquiryModalInstance.show();
    }

    const inquiryForm = document.getElementById('inquiryForm');
    const courseSelect = document.getElementById('course');

    if (inquiryForm && courseSelect) {
        loadCoursesForDropdown(courseSelect);

        inquiryForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            await submitInquiryForm(inquiryForm, inquiryModalInstance);
        });

        inquiryModalElement?.addEventListener('show.bs.modal', () => {
            setFormMessage('', 'secondary');
        });
    }
});
