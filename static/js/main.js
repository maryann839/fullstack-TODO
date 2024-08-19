
// Added event listner for the websites
document.addEventListener('DOMContentLoaded', function() {

         //Get menuBtn and connect it with js to display menubar
      const  menuBtn = document.querySelector('.menu-btn')
      const  menuSection = document.querySelector('.menu-section')
      // Added a click event
      menuBtn.addEventListener('click', function() {
         menuSection.classList.toggle("active")
      })

      //This toggles the add new task button to display the task input
      const  addBtn = document.querySelector('.add-btn')
      const  asideMain = document.querySelector('.aside')

      addBtn.addEventListener('click', function() {
         if(asideMain.style.display === 'none' || asideMain.style.display ==='') {
            asideMain.style.display = 'block'
         } else {
            asideMain.style.display = 'none'
         }

      })

      const taskSection = document.querySelector('.my-task-section');

      addBtn.addEventListener('click', function() {
         // Toggle the visibility of the task section
         taskSection.classList.toggle('hidden');
        
      });
      
      // This gets each menu button to display the corresponding section
      // get the classes
      const  menuButtons = document.querySelectorAll('.menu-section button')
      const  sections = document.querySelectorAll('main > section:not(.menu-section)')
         
      
      menuButtons.forEach((button, index)=> {
         button.addEventListener('click', function() {
            // Hide the sessions
         sections.forEach((section, sectionIndex) =>{
               section.style.display = index === sectionIndex ? 'block' : 'none'
            })
            
         })
         
      });   

})




