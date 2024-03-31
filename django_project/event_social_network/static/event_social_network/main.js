//this function help with date selector over crispy forms. In event creating forms //
document.addEventListener("DOMContentLoaded", function() {
    var dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(function(input) {
        input.classList.add('custom-date-input');
        input.placeholder = 'Select date...';
    });
});
