const optionSelect = document.getElementById('default');
const dependentSelect = document.getElementById('specialYears');
const dependentSelect1 = document.getElementById('moreSpecialChars');
const dependentSelect2 = document.getElementById('numRange');
const dependentSelect3 = document.getElementById('wcRange');
const dependentSelect4 = document.getElementById('threshold');

function toggleDependentSelect() {
  if (optionSelect.value === 'n') {
    dependentSelect.disabled = false;
    dependentSelect1.disabled = false;
    dependentSelect2.disabled = false;
    dependentSelect3.disabled = false;
    dependentSelect4.disabled = false;
  } else {
    dependentSelect.disabled = true;
    dependentSelect1.disabled = true;
    dependentSelect2.disabled = true;
    dependentSelect3.disabled = true;
    dependentSelect4.disabled = true;
  }
};

// Call the function on page load
window.addEventListener('load', toggleDependentSelect);

// Add event listener to the select element
optionSelect.addEventListener('change', toggleDependentSelect);