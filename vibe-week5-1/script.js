const koreanMenus = [
  "김치찌개",
  "된장찌개",
  "비빔밥",
  "불고기",
  "제육볶음",
  "닭갈비",
  "떡볶이",
  "칼국수",
  "삼계탕",
  "김치볶음밥",
  "순두부찌개",
  "보쌈",
];

const recommendButton = document.querySelector("#recommend-button");
const menuResult = document.querySelector("#menu-result");

recommendButton.addEventListener("click", () => {
  const randomIndex = Math.floor(Math.random() * koreanMenus.length);
  menuResult.textContent = koreanMenus[randomIndex];
});
