const groups = document.querySelectorAll(".question-group"),
  nextBtn = document.getElementById("nextBtn"),
  submitBtn = document.getElementById("submitBtn"),
  bar = document.getElementById("bar");
let current = 0;

function showGroup(i) {
  groups.forEach((g, idx) => g.classList.toggle("hidden", idx !== i));
  bar.style.width = ((i + 1) / groups.length) * 100 + "%";
  nextBtn.classList.toggle("hidden", i === groups.length - 1);
  submitBtn.classList.toggle("hidden", i !== groups.length - 1);
}

nextBtn.onclick = () => {
  if (
    [...groups[current].querySelectorAll("fieldset")].some(
      (f) => !f.querySelector("input:checked")
    )
  ) {
    alert("من فضلك أجب عن جميع الأسئلة قبل المتابعة");

    return;
  }
  current++;
  showGroup(current);
};

showGroup(current);
