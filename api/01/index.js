let page = 1;
let API_URL = 'https://api.punkapi.com/v2/beers';
const plusButton = document.querySelector('#next');
const minusButton = document.querySelector('#prev');
const voltageInput = document.querySelector('.voltageInput');
const lessButton = document.querySelector('#less');
const moreButton = document.querySelector('#more');
const container = document.querySelector('.container');

const render = (data) => {
  if (!data.length) return;
  const fragment = document.createDocumentFragment();
  data.forEach (({ name, tagline, description, image_url: imageURL, abv }) => {
    const div = document.createElement('div');
    div.classList.add('beer');
    div.innerHTML = `
    <div class="beer--content">
      <h1 class="beer--title">${name} ${abv}%</h1>
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

const removeElements = () => {
  const previousElements = document.querySelectorAll('.beer');
  previousElements.forEach(element => element.remove());
}

const buttonsControl = () => {
  if(page === 13) {
    document.getElementById('next').disabled = true;
  } else {
    document.getElementById('next').disabled = false;
  }
  if(page === 1) {
    document.getElementById('prev').disabled = true;
  } else {
    document.getElementById('prev').disabled = false;
  }
}

const pagination = (sign) => {
  if (sign === 'next') page += 1;
  if (sign === 'prev') page -= 1;

  API_URL = `https://api.punkapi.com/v2/beers?page=${page}`;

  removeElements();
  getData(API_URL);

  let label = document.querySelector('.pageLabel');
  label.innerHTML = `PageNo ${page}/13`;

  buttonsControl();
}

const filterVoltage = (type, voltage) => {
  if (type === 'less') API_URL = `https://api.punkapi.com/v2/beers?abv_lt=${voltage}`;
  if (type === 'more') API_URL = `https://api.punkapi.com/v2/beers?abv_gt=${voltage}`;
  removeElements();
  getData(API_URL);
}

getData(API_URL);
plusButton.addEventListener('click', () => { pagination(plusButton.id)});
minusButton.addEventListener('click', () => { pagination(minusButton.id)});
lessButton.addEventListener('click', () => { filterVoltage(lessButton.id, voltageInput.value)});
moreButton.addEventListener('click', () => { filterVoltage(moreButton.id, voltageInput.value)});