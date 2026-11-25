// 들꽃상점 작은 스크립트 (연습용)
const hours = { 평일: "10:00 ~ 20:00", 주말: "11:00 ~ 18:00" };

function todayLabel() {
  const day = new Date().getDay();
  return (day === 0 || day === 6) ? "주말" : "평일";
}

// 오늘 영업시간을 화면에 보여 줘요
const label = todayLabel();
document.getElementById("open-time").textContent = hours[label] + " (" + label + ")";

// 장바구니 개수를 보여 줘요
document.getElementById("cart-count").textContent = "0";

console.log("들꽃상점 스크립트 끝까지 실행됨");
