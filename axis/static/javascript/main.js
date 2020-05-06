console.log("This is Captain Kirk speaking.")

//////// functions to get project id and attach it to posts for updates
let projectId;
let allUpdateButtons = document.querySelectorAll(".openUpdateModal");
allUpdateButtons.forEach( (ele) => {
	ele.addEventListener('click', setProjectId);
});
//update route to use the correct project id 
function setProjectId (event) {
    projectId = event.target.getAttribute('data-projectid');
    projectId = projectId.replace('q','');
    document.projectUpdateForm.action = `project/${projectId}/update`
    let formname = document.querySelector('#updateName');
    let formdis = document.querySelector('#updateDescription');
    //
    formname.value = document.querySelector('span[class*="' + projectId +'"]').textContent;
    formdis.value = document.querySelector('p[class*="' + projectId +'"]').textContent;
}
// take the values from the page and put them in the form 
// get the element and then set the value 


