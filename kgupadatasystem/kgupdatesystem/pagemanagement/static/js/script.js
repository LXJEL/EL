$(document).ready(function() {
  $("#gotopage").click(function() {
    var selectPage = document.getElementById("select-page");
    var kg_id = selectPage.value;
    if (kg_id) {
      window.location.href = "../visual/";
    } else {
      alert("请选择需要跳转的页面！");
    }
  });
});
