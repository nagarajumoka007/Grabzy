import {updateCartQuantity,
    updateAddToCartButtonHtml, 
    getCookies } from "../../../../static/JavaScript/utils.js"


// async function fetchCartData(){
//     try{
//         const response = await fetch('/cart/details/')
//         const data = await response.json()
//         return data
//     } catch(e){
//         console.error(e)
//     }
// }



function initCartButton(url){
    // const addToCartElements = document.querySelectorAll(".js-update-quantity")
    if(url.includes('search')){
        // console.log('search')
        // const searchInputElement = document.querySelector('.js-search-input')
        // searchInputElement.value = new URL(window.location.href).searchParams.get('search')
        // document.querySelector(".choose-items-grid").addEventListener('click', async (event) => {
        // if(event.target.classList.contains('js-update-quantity')){
        //     const item = event.target
        //     const productPID = item.dataset.productId
        //     const sub = item.dataset.sub === 'true' ? true : false
        //     const data = await updateCartQuantity(productPID, sub)
        //     updateAddToCartButtonHtml(data)
        //     }
        // })
    } else if(url.includes('cart')){
        // console.log('cart')
        // const cartElement = document.querySelector(".cart-content")
        // if(!cartElement) return
        // cartElement.addEventListener('click', async (event) => {
        // if(event.target.classList.contains('js-update-quantity')){
        //     const item = event.target
        //     const productPID = item.dataset.productId
        //     const sub = item.dataset.sub === 'true' ? true : false
        //     console.log(productPID, sub)
        //     const data = await updateCartQuantity(productPID, sub)
        //     updateCartDynamicButton(data)
        //     updateSubTotalInPayment()
        //     } else if(event.target.classList.contains('js-cartitem-delete')){
        //         const pid = event.target.dataset.productId
        //         const endpoint = `/cart/delete/${pid}/`
        //         const response = await fetch(endpoint)
        //         const data = await response.json()
        //         const cartItemElement = document.querySelector(`.js-cart-grid-${pid}`)
        //         cartItemElement.remove()
        //         const horizontalLine = document.querySelector(`.js-horizontal-line-${pid}`)
        //         horizontalLine.remove()
        //         const cartContentElement = document.querySelector('.js-cart-content')
        //         if(data.cart_count === 0 && cartContentElement){
        //             cartContentElement.classList.add('empty-cart-container')
        //             cartContentElement.classList.remove('cart-content')
        //             cartContentElement.innerHTML = `<p class="cart-empty-text">Your cart is empty</p>`
        //         }
        //         updateSubTotalInPayment()
        //         updateCartItemsCount(data.cart_count)

        //     }
        // })
        // updateSubTotalInPayment()
    } else if(url.includes('category')){
        // console.log('category')
        // document.querySelector(".choose-items-grid").addEventListener('click', async (event) => {
        // if(event.target.classList.contains('js-update-quantity')){
        //     const item = event.target
        //     const productPID = item.dataset.productId
        //     const sub = item.dataset.sub === 'true' ? true : false
        //     const data = await updateCartQuantity(productPID, sub)
        //     updateAddToCartButtonHtml(data)
        //     }
        // })
    } else if(url.includes('product')){
        console.log('Product')
        // document.querySelector(".product-container").addEventListener('click', async (event) => {
        // if(event.target.classList.contains('js-update-quantity')){
        //     const item = event.target
        //     const productPID = item.dataset.productId
        //     const sub = item.dataset.sub === 'true' ? true : false
        //     const data = await updateCartQuantity(productPID, sub)
        //     console.log(data)
        //     updateAddToCartButtonHtml(data)
        //     } else if(event.target.classList.contains('js-buy-now')) {
        //         console.log('Clicked on Buy Now')
        //         const productPid = event.target.dataset.productId
        //         try{
        //             const response = await fetch(`/cart/buy-now/${productPid}/`)
        //             const data = await response.json()
        //             updateCartItemsCount(data.cart_count)
        //             window.location.href = "/cart/"
        //             if(data.status !== 'success'){
        //                 alert("Something is wrong...")
        //             }
        //         } catch(e) {
        //             alert("Something is wrong...")
        //         }
                
        //     }
        // })
    } 

}

console.log(window.location.pathname)


if(window.location.pathname === '/search/' || window.location.pathname === '/cart/' || window.location.pathname.includes('/category/') || window.location.pathname.includes('/product/') ){
    document.addEventListener('DOMContentLoaded', initCartButton(window.location.pathname));
}

const homePageElement = document.querySelector(".scrollabale-items-grid")
if(homePageElement){
    document.querySelector(".scrollabale-items-grid").addEventListener('click', async (event) => {
        if(event.target.classList.contains('js-update-quantity')){
            const item = event.target
            const productPID = item.dataset.productId
            const sub = item.dataset.sub === 'true' ? true : false
            const data = await updateCartQuantity(productPID, sub)
            console.log(data)
            updateAddToCartButtonHtml(data)
            }
        })
}

// const profileEditElement = document.querySelector(".js-edit-information-button")
// if(profileEditElement){
//     profileEditElement.addEventListener("click", async (event) => {
//         const userId = profileEditElement.dataset.userPk
//         console.log(userId)
//         const response = await fetch(`/users/${userId}/`)
//         const data = await response.json()
//         console.log(data)

//         const profileElement = document.querySelector(".profile")
//         profileElement.innerHTML = `
//             <h3>Account Information</h3>
//                 <form method="POST" enctype="multipart/form-data" action="" id="profile-update-form">
//                     <button class="save-information-button js-save-information-button" type="submit">Save</button>
//                     <button class="cancel-information-button js-cancel-information-button">Cancel</button>
//                     <div class="account-section">

//                         <div class="profile-image-container">
//                             <img src="${data.profile}" alt="" class="profile-image js-profile-image">
//                             <label for="image-upload">
//                                 <img src="../../../static/images/camera-reverse-outline.svg" class="image-upload-button" title="Upload Image">
//                             </label>
                            
//                             <input type="file" accept="image/*" id="image-upload" name="profile" class="image-upload-input js-image-upload">
//                         </div>
                        
//                         <div class="account-information-inputs">
//                             <div>
//                                 <label for="id-username" class="username-label">Username: </label>
//                                 <input type="text" id="id-username" name="username" value="${data.username}">
//                             </div>
                            
//                             <div>
//                                 <label for="id-email" class="email-label">Email: </label>
//                                 <input type="email" id="id-email" name="email" value="${data.email}">
//                             </div>
                            
//                         </div>

//                     </div>
//                 </form>
//         `
//         const cancelButtonElement = document.querySelector(".js-cancel-information-button")
//         if(cancelButtonElement){
//             cancelButtonElement.addEventListener("click", () => {
//                 profileElement.innerHTML = `
//                 <h3>Account Information</h3>
//                 <button class="edit-information-button js-edit-information-button" data-user-pk = "${userId}">Edit Information</button>
//                 <div class="account-section">
//                     <div class="profile-image-container">
//                         <img src="${data.profile}" alt="" class="profile-image">
//                     </div>
//                     <div>
//                         <p>${data.username}</p>
//                         <p class="profile-email">${data.email}</p>
//                     </div>
//                 </div>
//             `
//             })
//         }

//         const uploadImageElement = document.querySelector(".js-image-upload")
//         let profileImage;
//         if(uploadImageElement){
//             uploadImageElement.addEventListener("change", (event) => {
//                 profileImage = event.target.files[0]
//                 console.log(profileImage)
//                 const file = URL.createObjectURL(profileImage)
//                 document.querySelector(".js-profile-image").src = file
//             })
//         }

//         const profileDataFormElement = document.querySelector("#profile-update-form")
//         if(profileDataFormElement){
//             profileDataFormElement.addEventListener('submit', async (event)=>{
//                 event.preventDefault()
//                 const form  = event.target
//                 const formData = new FormData(form)
//                 const profileUpdateResponse = await fetch(`/users/${userId}/`, {
//                 method: 'POST',
//                 headers: {
//                     // "Content-Type": "application/json",
//                     "X-CSRFToken": getCookies("csrftoken")
//                 },
//                 body: formData
//                 })

//                 const profileUpdateData = await profileUpdateResponse.json()
//                 console.log(profileUpdateData)

//                 profileElement.innerHTML = `
//                 <h3>Account Information</h3>
//                 <button class="edit-information-button js-edit-information-button" data-user-pk = "${userId}">Edit Information</button>
//                 <div class="account-section">
//                     <div class="profile-image-container">
//                         <img src="${profileUpdateData.profile}" alt="" class="profile-image">
//                     </div>
//                     <div>
//                         <p>${profileUpdateData.username}</p>
//                         <p class="profile-email">${profileUpdateData.email}</p>
//                     </div>
//                 </div>
//             `
//                 const navProfileImageElement = document.querySelector(".js-nav-user-profile")
//                 if(navProfileImageElement){
//                     navProfileImageElement.src = profileUpdateData.profile
//                 }
//             })
            
//         }
        
//     })
// }


// CartObject.updateCartNumber();