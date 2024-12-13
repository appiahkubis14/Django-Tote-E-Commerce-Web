// Function to fetch data from the API
const fetchData = async (url) => {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return await response.json();
    } catch (error) {
      console.error('Fetch error:', error);
      alert('Error fetching product data. Please try again later.');
    }
  };
  
  const renderProducts = (products) => {
    const productContainer = document.querySelector('#latest-item .row');  // Select the product container
    productContainer.innerHTML = '';  // Clear any previous products
    products.forEach(product => {
      const productElement = `
        <div class="col-xxl-3 col-xl-4 col-md-6">
          <div class="product__item bor">
            <a href="#0" class="wishlist">
              <i class="fa-regular fa-heart"></i>
            </a>
            <a href="shop-single/" class="product__image pt-20 d-block">
              <img class="font-image" src="${product.image}" alt="image" />
              <img class="back-image" src="${product.image}" alt="image" />
            </a>
            <div class="product__content">
              <h4 class="mb-15">
                <a class="primary-hover" href="shop-single/">${product.name}</a>
              </h4>
              <del>$${product.old_price}</del>
              <span class="primary-color ml-10">$${product.new_price}</span>
              <div class="star mt-20">
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
              </div>
            </div>
            <a class="product__cart d-block bor-top" href="#0">
              <i class="fa-regular fa-cart-shopping primary-color me-1"></i>
              <span>Add to cart</span>
            </a>
          </div>
        </div>
      `;
      productContainer.innerHTML += productElement; 
       // Append each product's HTML to the container
    });
  };


  let swiperInitialized = false; // Prevent multiple Swiper initializations
  
  const renderGallery = (products) => {
    const gallerySlider = document.getElementById('slider'); // Select the gallery swiper container
    gallerySlider.innerHTML = ''; // Clear any previous items
  
    let galleryHTML = ''; // Store all the gallery items in a string first
  
    products.forEach((product) => {
      const image = product.image || 'path/to/default-image.jpg'; // Fallback for missing image
      const name = product.name || 'Product Name'; // Fallback for missing name
      const description = product.description || 'Product Description'; // Fallback for missing description
  
      galleryHTML += `
        <div class="swiper-slide">
          <div class="gallery__item">
            <div class="off-tag">50% <br /> off</div>
            <div class="gallery__image image">
              <img src="${image}" alt="${name}" />
            </div>
            <div class="gallery__content">
              <h3 class="mb-10"><a href="shop-2/">${name}</a></h3>
              <p>${description}</p>
              <a href="shop-2/" class="btn-two mt-25"><span>Shop Now</span></a>
            </div>
          </div>
        </div>
      `;
    });
  
    gallerySlider.innerHTML = galleryHTML; // Update the gallery in one go
  
    if (!swiperInitialized) {
        new Swiper('.gallery__slider', {
          loop: true,
          slidesPerView: 1,
          spaceBetween: 10,
          autoplay: {
            delay: 5000,
          },
          breakpoints: {
            768: {
              slidesPerView: 2,
              spaceBetween: 20,
            },
            1024: {
              slidesPerView: 3,
              spaceBetween: 30,
            },
          },
        });
        swiperInitialized = true;  // Mark Swiper as initialized
      }
  };
  


  
  const initFrontend = async () => {
    try {
      const products = await fetchData('http://192.168.100.251:8000/api/products/');  // Fetch products from the API
      renderProducts(products);  // Render the fetched products into the template
      renderGallery(products);  // Render the fetched gallery items into the gallery template
    } catch (error) {
      console.error('Error initializing frontend:', error);
    }
  };
  document.addEventListener('DOMContentLoaded', initFrontend);
  
  

  //=================================================================



  async function fetchCategories() {
    try {
        // Fetching the data from the Django API
        const response = await fetch('http://192.168.100.251:8000/api/categories/');
        const categories = await response.json();

        const marqueeList = document.getElementById('marquee-list');
        marqueeList.innerHTML = '';  // Clear any existing content

        // Loop through categories and add them to the marquee
        categories.forEach(category => {
            // Create the category item
            const listItem = document.createElement('li');
            listItem.classList.add('marquee-item');

            // Add the category name and icon
            listItem.innerHTML = `
                ${category.name}
                <img  src="/static/portal/assets/images/icon/title-left.svg" alt="icon" />
            `;

            // Append the list item to the marquee
            marqueeList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error fetching categories:', error);
    }
}

// Call the function to fetch and populate the categories when the page loads
window.onload = fetchCategories;