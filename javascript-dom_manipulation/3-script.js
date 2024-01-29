document.addEventListener('DOMContentLoaded', function() {
  const toggleHeaderElement = document.getElementById('toggle_header');
  const headerElement = document.querySelector('header');

  toggleHeaderElement.addEventListener('click', function() {
    headerElement.classList.toggle('red');
    headerElement.classList.toggle('green');
  });
});
