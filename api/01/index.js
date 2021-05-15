let page = 1;
let API_URL = `https://api.punkapi.com/v2/beers?page=${page}`;
const plusButton = document.querySelector('#next');
const minusButton = document.querySelector('#prev');
const container = document.querySelector('.container');

const render = (data) => {
  if (!data.length) return;
  const fragment = document.createDocumentFragment();
  data.forEach (({ name, tagline, description, image_url: imageURL }) => {
    const div = document.createElement('div');
    div.classList.add('beer');
    div.innerHTML = `
    <div class="beer--content">
      <h1 class="beer--title">${name}</h1>
      <p class="beer--tagline">${tagline}</p>
      <p class="beer--description">${description}</p>
    </div>
    <img class="beer--image" src="${imageURL}">
    `;
    fragment.appendChild(div);
  });
  container.appendChild(fragment);
}

const success = (response) => response.json()

const error = (err) => {
  console.log(err);
}
const getData = (url) => {
  fetch(url)
  .then(success)
  .then(render)
  .catch(error);
}

const pagination = (sign) => {
  if (sign === 'next') page += 1;
  if (sign === 'prev') page -= 1;

  API_URL = `https://api.punkapi.com/v2/beers?page=${page}`;

  const previousElements = document.querySelectorAll('.beer');
  previousElements.forEach(element => element.remove());
  document.querySelector('.pageLabel') ? document.querySelector('.pageLabel').remove() : null;

  getData(API_URL);

  const parent = document.querySelector('.controls');
  const label = document.createElement('p');
  label.classList.add('pageLabel');
  label.innerHTML = `PageNo ${page}`;
  parent.appendChild(label);

  if(page === 13) {
    alert('This is last page!');
  }
}

getData(API_URL);
plusButton.addEventListener('click', () => { pagination(plusButton.id)});
minusButton.addEventListener('click', () => { pagination(minusButton.id)});