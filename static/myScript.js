// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()

// document.addEventListener('click', function handleClick(event) {
//   // console.log('user clicked: ', event.target);

//   if (event.target.classList.contains('bg-success')) {
//     event.target.classList.remove('bg-success');
//   } else {
//     event.target.classList.add('bg-success');
//   }
// });


const rows = document.querySelectorAll('tbody > tr');

for (const row of rows) {
  row.addEventListener('click', function handleClick() {
    if (row.classList.contains('bg-success')) {
      row.classList.remove('bg-success');
    } else {
      row.classList.add('bg-success');
    }
  });
}

