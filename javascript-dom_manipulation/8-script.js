document.addEventListener('DOMContentLoaded', async function() {
  const helloElement = document.getElementById('hello');

  try {
    const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    helloElement.textContent = data.hello;
  } catch (error) {
    console.error('Error fetching hello translation:', error.message);
  }
});
