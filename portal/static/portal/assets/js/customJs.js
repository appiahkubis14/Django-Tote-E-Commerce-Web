// // Generic function to fetch data from the API with error handling
// const fetchData = async (url) => {
//   try {
//     const response = await fetch(url);
//     if (!response.ok) {
//       throw new Error(`Network response was not ok, status: ${response.status}`);
//     }
//     return await response.json();
//   } catch (error) {
//     console.error(`Fetch error for URL ${url}:`, error);
//     alert('Error fetching data. Please try again later.');
//     return [];  // Return an empty array if there's an error fetching the data
//   }
// };



// //==============================================================================================================================
// // Function to render the products for the first container
// // const renderProducts = (products) => {
// //   console.log("Products received:", products);

// //   const latestItemContainer = document.querySelector('#latest-item .row');
// //   if (!latestItemContainer) {
// //     console.error("Container element not found in the DOM.");
// //     return;
// //   }

// //   latestItemContainer.innerHTML = '';
  
// //   products.forEach((product) => {
// //     const productElement = `
// //       <div class="col-xxl-3 col-xl-4 col-md-6">
// //         <div class="product__item bor">
// //           <a href="#0" class="wishlist">
// //             <i class="fa-regular fa-heart"></i>
// //           </a>
// //           <a href="shop-single/" class="product__image pt-20 d-block">
// //             <img class="font-image" src="${product.image || 'path/to/default-image.jpg'}" alt="image" />
// //             <img class="back-image" src="${product.image || 'path/to/default-image.jpg'}" alt="image" />
// //           </a>
// //           <div class="product__content">
// //             <h4 class="mb-15">
// //               <a class="primary-hover" href="shop-single/">${product.name || 'Product Name'}</a>
// //             </h4>
// //             <del>₵${product.old_price || '0.00'}</del>
// //             <span class="primary-color ml-10">₵${product.new_price || '0.00'}</span>
// //             <div class="star mt-20">
// //               <i class="fa-solid fa-star"></i>
// //               <i class="fa-solid fa-star"></i>
// //               <i class="fa-solid fa-star"></i>
// //               <i class="fa-solid fa-star"></i>
// //               <i class="fa-solid fa-star"></i>
// //             </div>
// //           </div>
// //           <a class="product__cart d-block bor-top" data-product-id="{{ product.id }}" style="cursor: pointer;>
// //             <i class="fa-regular fa-cart-shopping primary-color me-1"></i>
// //             <span>Add to cart</span>
// //           </a>
// //         </div>
// //       </div>
// //     `;
// //     latestItemContainer.innerHTML += productElement;
// //   });
// // };



// //==============================================================================================================================

// const renderProductList = (products) => {
//   const productListContainer = document.querySelector('#productList .row');
//   if (!productListContainer) {
//     console.error("productList element not found in the DOM.");
//     return;
//   }
//   productListContainer.innerHTML = '';

//   products.forEach((product) => {
//     const productElement = `
//       <div class="col-xl-4 col-lg-6 col-md-6">
//         <div class="product__item bor">
//           <a href="#0" class="wishlist">
//             <i class="fa-regular fa-heart"></i>
//           </a>
//           <a href="shop-single.html" class="product__image pt-20 d-block">
//             <img class="font-image" src="${product.image || 'path/to/default-image.jpg'}" alt="image" />
//             <img class="back-image" src="${product.image || 'path/to/default-image.jpg'}" alt="image" />
//           </a>
//           <div class="product__content">
//             <h4 class="mb-15">
//               <a class="primary-hover" href="shop-single.html">${product.name || 'Product Name'}</a>
//             </h4>
//             <del>₵${product.old_price || '0.00'}</del>
//             <span class="primary-color ml-10">₵${product.new_price || '0.00'}</span>
//             <div class="star mt-20">
//               <i class="fa-solid fa-star"></i>
//               <i class="fa-solid fa-star"></i>
//               <i class="fa-solid fa-star"></i>
//               <i class="fa-solid fa-star"></i>
//               <i class="fa-solid fa-star"></i>
//             </div>
//           </div>
//           <a class="product__cart d-block bor-top" style="cursor: pointer; data-product-id="{{ product.id }}">
//             <i class="fa-regular fa-cart-shopping primary-color me-1"></i>
//             <span>Add to cart</span>
//           </a>
//         </div>
//       </div>
//     `;
//     productListContainer.innerHTML += productElement;
//   });
// };



// //==============================================================================================================================
// let swiperInitialized = false; 
// const renderGallery = (products) => {
//   const gallerySlider = document.getElementById('slider');
//   gallerySlider.innerHTML = ''; 

//   let galleryHTML = ''; 
//   products.forEach((product) => {
//     const image = product.image || 'path/to/default-image.jpg'; 
//     const name = product.name || 'Product Name'; 
//     const description = product.description || 'Product Description'; 

//     galleryHTML += `
//       <div class="swiper-slide">
//         <div class="gallery__item">
//           <div class="off-tag">50% <br /> off</div>
//           <div class="gallery__image image">
//             <img src="${image}" alt="${name}" />
//           </div>
//           <div class="gallery__content">
//             <h3 class="mb-10"><a href="shop-2/">${name}</a></h3>
//             <p>${description}</p>
//             <a class="product__cart d-block bor-top" style="cursor: pointer; data-product-id="{{ product.id }}" class="btn-two mt-25" ">
//             <span>
//             Shop Now
//             </span>
//             </a>
//           </div>
//         </div>
//       </div>
//     `;
//   });

//   gallerySlider.innerHTML = galleryHTML; 
//   if (!swiperInitialized) {
//       new Swiper('.gallery__slider', {
//         loop: true,
//         slidesPerView: 1,
//         spaceBetween: 10,
//         autoplay: {
//           delay: 5000,
//         },
//         breakpoints: {
//           768: {
//             slidesPerView: 2,
//             spaceBetween: 20,
//           },
//           1024: {
//             slidesPerView: 3,
//             spaceBetween: 30,
//           },
//         },
//       });
//       swiperInitialized = true; 
//     }
// };


// //==============================================================================================================================

// let currentPage = 1; 
// const totalPages = 5;

// const renderPagination = (currentPage, totalPages) => {
//   const paginationContainer = document.querySelector('.pagi-wrp');
//   if (!paginationContainer) return;

//   paginationContainer.innerHTML = ''; 

//   for (let i = 1; i <= totalPages; i++) {
//     const activeClass = i === currentPage ? 'active' : '';
//     const pageElement = `<a href="#0" class="pagi-btn ${activeClass}" data-page="${i}">${i}</a>`;
//     paginationContainer.innerHTML += pageElement;
//   }
 
//   if (currentPage < totalPages) {
//     paginationContainer.innerHTML += `
//       <a href="#0" class="fa-regular ms-2 primary-hover fa-angle-right" data-page="${currentPage + 1}"></a>
//     `;
//   }

//   const pageLinks = paginationContainer.querySelectorAll('.pagi-btn');
//   pageLinks.forEach(link => {
//     link.addEventListener('click', (event) => {
//       const page = parseInt(event.target.dataset.page);
//       if (page !== currentPage && page >= 1 && page <= totalPages) {
//         currentPage = page;
//         updatePage(); 
//       }
//     });
//   });

//   const nextButton = paginationContainer.querySelector('.fa-angle-right');
//   if (nextButton) {
//     nextButton.addEventListener('click', () => {
//       if (currentPage < totalPages) {
//         currentPage++;
//         updatePage(); 
//       }
//     });
//   }
// };

// const updatePage = async () => {
//   const products = await fetchData(`http://192.168.100.251:8000/api/products/?page=${currentPage}`);
  
//   renderProducts(products); 
//   renderPagination(currentPage, totalPages);
// };

// // Initial render
// renderPagination(currentPage, totalPages);




// //==============================================================================================================================
// // Initialize frontend and fetch products
// const initFrontend = async () => {
//   try {
//     const products = await fetchData('http://192.168.100.251:8000/api/products/'); 
//     if (products.length > 0) {
//       // renderProducts(products);
//       renderProductList(products);
//       renderPagination(1, 5);  // Example pagination
//       renderGallery(products);
//     }
//   } catch (error) {
//     console.error('Error initializing frontend:', error);
//   }
// };

// document.addEventListener('DOMContentLoaded', initFrontend);



// //==============================================================================================================================
// // Function to fetch and render categories
// async function fetchCategories() {
//   try {
//     const categories = await fetchData('http://192.168.100.251:8000/api/categories/');
//     const marqueeList = document.getElementById('marquee-list');
//     marqueeList.innerHTML = '';  // Clear existing list
//     categories.forEach(category => {
//       const listItem = document.createElement('li');
//       listItem.classList.add('marquee-item');
//       listItem.innerHTML = `
//         ${category.name}
//         <img src="/static/portal/assets/images/icon/title-left.svg" alt="icon" />
//       `;
//       marqueeList.appendChild(listItem);
//     });
//   } catch (error) {
//     console.error('Error fetching categories:', error);
//   }
// }

// window.onload = fetchCategories;




// //==============================================================================================================================

// // Event listener for Add to Cart
// document.querySelectorAll('.product__cart').forEach(button => {
//   button.addEventListener('click', async (e) => {
//     e.preventDefault();

//     const productId = button.getAttribute('data-product-id');
    
//     try {
//       const response = await fetch('http://192.168.100.251:8000/api/cart/add/', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//           'X-CSRFToken': getCsrfToken(),  // If you are using CSRF tokens
//         },
//         body: JSON.stringify({ product_id: productId })
//       });

//       if (response.ok) {
//         alert('Item added to cart!');
//         // Optionally update the UI to reflect the cart
//         updateCart();
//       } else {
//         alert('Failed to add item to cart.');
//       }
//     } catch (error) {
//       console.error('Error adding item to cart:', error);
//     }
//   });
// });

// // Helper function to get CSRF token (if needed)
// function getCsrfToken() {
//   const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//   return csrfToken;
// }

// // Function to update the cart (e.g., reload cart page or update cart icon)
// async function updateCart() {
//   const response = await fetch('http://192.168.100.251:8000/api/cart/');
//   if (response.ok) {
//     const cartItems = await response.json();
//     // Update your cart UI with the new cart items
//     renderCartItems(cartItems);
//   }
// }

// // Function to render cart items on the page
// function renderCartItems(cartItems) {
//   const cartContainer = document.querySelector('#cart-item');
//   cartContainer.innerHTML = '';  // Clear current cart items

//   cartItems.forEach(item => {
//     const itemHTML = `
//         <div class="product-details d-flex align-items-center">
//           <img src="${item.product_image}" alt="image" />
//           <h4 class="ps-4 text-capitalize">${item.product_name}</h4>
//         </div>
//         <div class="product-price">${item.price}</div>
//         <div class="product-quantity">
//           <input type="number" value="${item.quantity}" min="1" data-item-id="${item.id}" />
//         </div>
//         <div class="product-line-price">${item.line_price}</div>
//         <div class="product-removal">
//           <button class="remove-product" data-item-id="${item.id}">
//             <i class="fa-solid fa-x heading-color"></i>
//           </button>
//         </div>
      
//     `;
//     cartContainer.innerHTML += itemHTML;
//   });

//   // Add event listeners for removal buttons
//   document.querySelectorAll('.remove-product').forEach(button => {
//     button.addEventListener('click', async (e) => {
//       const itemId = button.getAttribute('data-item-id');
//       await removeFromCart(itemId);
//       updateCart();
//     });
//   });
// }

// // Function to remove an item from the cart
// async function removeFromCart(itemId) {
//   const response = await fetch(`http://192.168.100.251:8000/api/cart/${itemId}/delete/`, {
//     method: 'DELETE',
//     headers: {
//       'Content-Type': 'application/json',
//       'X-CSRFToken': getCsrfToken(),
//     }
//   });

//   if (!response.ok) {
//     alert('Failed to remove item from cart.');
//   }
// }

