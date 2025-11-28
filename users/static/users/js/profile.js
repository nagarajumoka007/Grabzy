import { makeAPICall, getCookies } from "../../../../static/JavaScript/utils.js"

const profileContainerElement = document.querySelector(".profile-main-container")
profileContainerElement.addEventListener('click', async (e) => {
    if(e.target.classList.contains('js-edit-information-button')){
        const profileEditElement = document.querySelector(".js-edit-information-button")
        const userId = profileEditElement.dataset.userPk
        console.log(userId)
        const response = await makeAPICall(`/users/${userId}/`, 'GET')
        const data = await response.json()
        console.log(data)

        const profileElement = document.querySelector(".profile")
        profileElement.innerHTML = `
            <h3>Account Information</h3>
                <form method="POST" enctype="multipart/form-data" action="" id="profile-update-form">
                    <button class="save-information-button js-save-information-button" type="submit">Save</button>
                    <button class="cancel-information-button js-cancel-information-button">Cancel</button>
                    <div class="account-section">

                        <div class="profile-image-container">
                            <img src="${data.profile}" alt="" class="profile-image js-profile-image">
                            <label for="image-upload">
                                <img src="../../../static/images/camera-reverse-outline.svg" class="image-upload-button" title="Upload Image">
                            </label>
                            
                            <input type="file" accept="image/*" id="image-upload" name="profile" class="image-upload-input js-image-upload">
                        </div>
                        
                        <div class="account-information-inputs">
                            <div>
                                <label for="id-username" class="username-label">Username: </label>
                                <input type="text" id="id-username" name="username" value="${data.username}">
                            </div>
                            
                            <div>
                                <label for="id-email" class="email-label">Email: </label>
                                <input type="email" id="id-email" name="email" value="${data.email}">
                            </div>
                            
                        </div>

                    </div>
                </form>
        `
        const cancelButtonElement = document.querySelector(".js-cancel-information-button")
        if(cancelButtonElement){
            cancelButtonElement.addEventListener("click", () => {
                profileElement.innerHTML = `
                <h3>Account Information</h3>
                <button class="edit-information-button js-edit-information-button" data-user-pk = "${userId}">Edit Information</button>
                <div class="account-section">
                    <div class="profile-image-container">
                        <img src="${data.profile}" alt="" class="profile-image">
                    </div>
                    <div>
                        <p>${data.username}</p>
                        <p class="profile-email">${data.email}</p>
                    </div>
                </div>
            `
            })
        }

        const uploadImageElement = document.querySelector(".js-image-upload")
        let profileImage;
        if(uploadImageElement){
            uploadImageElement.addEventListener("change", (event) => {
                profileImage = event.target.files[0]
                console.log(profileImage)
                const file = URL.createObjectURL(profileImage)
                document.querySelector(".js-profile-image").src = file
            })
        }

        const profileDataFormElement = document.querySelector("#profile-update-form")
        if(profileDataFormElement){
            profileDataFormElement.addEventListener('submit', async (event)=>{
                event.preventDefault()
                const form  = event.target
                const formData = new FormData(form)
                const body = formData
                const method = 'POST'
                const headers = {
                    // "Content-Type": "application/json",
                    "X-CSRFToken": getCookies("csrftoken")
                }
                const profileUpdateResponse = await makeAPICall(`/users/${userId}/`, method, body, headers)

                const profileUpdateData = await profileUpdateResponse.json()
                console.log(profileUpdateData)

                profileElement.innerHTML = `
                <h3>Account Information</h3>
                <button class="edit-information-button js-edit-information-button" data-user-pk = "${userId}">Edit Information</button>
                <div class="account-section">
                    <div class="profile-image-container">
                        <img src="${profileUpdateData.profile}" alt="" class="profile-image">
                    </div>
                    <div>
                        <p>${profileUpdateData.username}</p>
                        <p class="profile-email">${profileUpdateData.email}</p>
                    </div>
                </div>
            `
                const navProfileImageElement = document.querySelector(".js-nav-user-profile")
                if(navProfileImageElement){
                    navProfileImageElement.src = profileUpdateData.profile
                }
            })
            
        }
 
    }
})
