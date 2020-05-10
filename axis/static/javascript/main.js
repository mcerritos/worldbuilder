console.log("This is Captain Kirk speaking.")

//////// functions to get project id and attach it to project for updates
let projectId;
let allUpdateProjectButtons = document.querySelectorAll(".openUpdateModal");
allUpdateProjectButtons.forEach( (ele) => {
	ele.addEventListener('click', setProjectId);
});
//update route to use the correct project id 
function setProjectId (event) {
    projectId = event.target.getAttribute('data-projectid');
    projectId = projectId.replace('q','');
    document.projectUpdateForm.action = `project/${projectId}/update`
    //
    let formname = document.querySelector('#updateName');
    let formdis = document.querySelector('#updateDescription');
    //
    formname.value = document.querySelector('span[class*="' + projectId +'"]').textContent;
    formdis.value = document.querySelector('p[class*="' + projectId +'"]').textContent;
}

//////// functions to get post id for post update
let postId;
let allUpdatePostButtons = document.querySelectorAll(".openUpdatePost");
allUpdatePostButtons.forEach( (ele) => {
	ele.addEventListener('click', setPostId);
});
// update route on modal
function setPostId (event) {
    postId = event.target.getAttribute('data-postid');
    console.log(postId);
    postId = postId.replace('p','');
    document.postUpdateForm.action = `/culture/post/${postId}/update`
    // these functions get the information from the page and load it into the document
    let formtitle = document.querySelector('#id_title');
    let formtext = document.querySelector('#updateText');
    formtitle.value = document.querySelector('h4[class*="' + postId +'"]').textContent;
    formtext.value = document.querySelector('p[class*="' + postId +'"]').textContent;
}

// toggle questions
let questions = document.getElementById('questions')
let plusButton = document.getElementById('showQuestions');
let minusButton = document.getElementById('hideQuestions');
minusButton.addEventListener('click', hideQuestions);
plusButton.addEventListener('click', showQuestions);

function hideQuestions() {
    questions.style.display = "none";
    minusButton.style.display = "none";
    plusButton.style.display = "inline-block";
}

function showQuestions() {
    questions.style.display = "block";
    minusButton.style.display = "inline-block";
    plusButton.style.display = "none";
  
}


