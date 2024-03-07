$(function () {
  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: "get",
      dataType: "json",
      beforeSend: function () {
        $("#modal-function").modal("show");
      },
      success: function (data) {
        $("#modal-function .modal-content").html(data.html_form);
      },
    });
  };

  var saveForm = function (e) {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: "json",
      success: function (data) {
        if (data.form_is_valid) {
          console.log(data);
          $("#function-table tbody").html(data.html_function_list);
          $("#modal-function").modal("hide");
        } else {
          $("#modal-function .modal-content").html(data.html_form);
        }
      },
    });
    return false;
  };

  /* Binding */

  // close the modal
  $("#modal-function").on("click", "#btn-close-modal", function () {
    $("#modal-function").modal("hide");
  });

  // Create function
  $(".js-create-function").click(loadForm);
  $("#modal-function").on("submit", ".js-function-create-form", saveForm);

  // Update function
  $("#function-table").on("click", ".js-update-function", loadForm);
  $("#modal-function").on("submit", ".js-function-update-form", saveForm);

  // Delete function
  $("#function-table").on("click", ".js-delete-function", loadForm);
  $("#modal-function").on("submit", ".js-function-delete-form", saveForm);
});
