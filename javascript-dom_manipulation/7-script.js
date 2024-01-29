document.addEventListener('DOMContentLoaded', function() {
    const listMoviesElement = document.getElementById('list_movies');

    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        const movieTitles = data.results.map(movie => movie.title);

        movieTitles.forEach(title => {
          const listItem = document.createElement('li');
          listItem.textContent = title;
          listMoviesElement.appendChild(listItem);
        });
      })
      .catch(error => {
        console.error('Error fetching movies:', error.message);
      });
  });
