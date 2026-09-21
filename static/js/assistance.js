
"use strict";

document.addEventListener("DOMContentLoaded", () => {
    const steps = document.querySelectorAll(".assistance-step");
    const backButton = document.getElementById("assistance-back");
    const nextButton = document.getElementById("assistance-next");
    const cancelLink = document.getElementById("assistance-cancel");
    const progressText = document.querySelector(".assistance-progress p");
    const progressBar = document.querySelector(".assistance-progress progress");

    let currentStep = 0;
    let editingFromReview = false;

    function populateReview() {
        const reviewSections = [
            {
                step: 0,
                target: "review-vehicle"
            },
            {
                step: 1,
                target: "review-problem"
            },
            {
                step: 2,
                target: "review-location"
            },
            {
                step: 3,
                target: "review-occupants"
            },
            {
                step: 4,
                target: "review-contact"
            }
        ];

        reviewSections.forEach(({ step, target }) => {
            const reviewContainer = document.getElementById(target);
            const fields = steps[step].querySelectorAll(
                "input, select, textarea"
            );

            reviewContainer.replaceChildren();

            fields.forEach((field) => {
                const label = steps[step].querySelector(
                    `label[for="${field.id}"]`
                );

                if (!label) {
                    return;
                }

                let value = field.value.trim();

                if (field.tagName === "SELECT" && value) {
                    value = field.selectedOptions[0].textContent.trim();
                }

                const row = document.createElement("p");
                const heading = document.createElement("strong");

                heading.textContent = `${label.textContent.trim()}: `;
                row.appendChild(heading);

                row.appendChild(
                    document.createTextNode(value || "Not provided")
                );

                reviewContainer.appendChild(row);
            });
        });
    }

    function showStep(stepIndex) {
    steps.forEach((step, index) => {
        step.hidden = index !== stepIndex;
    });

    currentStep = stepIndex;

    if (currentStep === steps.length - 1) {
        populateReview();
    }

    progressText.textContent = `Step ${currentStep + 1} of 6`;
    progressBar.value = currentStep + 1;

    backButton.hidden = currentStep === 0;
    cancelLink.hidden = currentStep !== 0;

    if (editingFromReview) {
        nextButton.textContent = "Return to Review";
    } else if (currentStep === steps.length - 1) {
        nextButton.textContent = "Submit Request";
    } else {
        nextButton.textContent = "Continue";
    }
}
        

    function validateCurrentStep() {
        const fields = steps[currentStep].querySelectorAll(
            "input, select, textarea"
        );

        for (const field of fields) {
            if (!field.checkValidity()) {
                field.reportValidity();
                field.focus();
                return false;
            }
        }

        return true;
    }

    nextButton.addEventListener("click", () => {
        if (!validateCurrentStep()) {
            return;
        }

        if (editingFromReview) {
            editingFromReview = false;
            showStep(steps.length - 1);
            return;
        }

        if (currentStep < steps.length - 1) {
            showStep(currentStep + 1);
        }
    });

    backButton.addEventListener("click", () => {
        if (currentStep > 0) {
            showStep(currentStep - 1);
        }
    });

    const editButtons = document.querySelectorAll(".assistance-edit");

    editButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const stepIndex = Number(button.dataset.editStep);

            if (
                Number.isInteger(stepIndex) &&
                stepIndex >= 0 &&
                stepIndex < steps.length - 1
            ) {
               editingFromReview = true;
               showStep(stepIndex); 
            }
        });
    });

    showStep(0);
    
});