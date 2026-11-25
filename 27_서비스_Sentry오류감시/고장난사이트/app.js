// 몽글 공방 주문 페이지 - 연습용 (버그 3개가 숨어 있어요)

const 장바구니 = [];

const 클래스목록 = [
  { 이름: "원데이 컵 만들기", 가격: 35000 },
  { 이름: "접시 물레 체험", 가격: 45000 },
];

function 결과보여주기(글) {
  document.getElementById("결과").textContent = 글;
}

function addToCart(상품) {
  장바구니.push(상품);
  결과보여주기(`${상품.이름}을(를) 담았어요. 지금 ${장바구니.length}개`);
}

// ① 장바구니 담기
document.getElementById("담기").addEventListener("click", function () {
  addToCrat(클래스목록[0]);
});

// ② 합계 보기
document.getElementById("합계").addEventListener("click", function () {
  let 합계 = 0;
  for (const 상품 of 클래스목록) {
    합계 += 상품.price;
  }
  결과보여주기("합계: " + 합계.toLocaleString("ko-KR") + "원 (예상: 80,000원)");
  if (Number.isNaN(합계)) {
    throw new Error("합계가 숫자가 아니에요: " + 합계);
  }
});

// ③ 저장된 예약 날짜 불러오기
document.getElementById("예약").addEventListener("click", function () {
  const 저장된글 = "{'날짜': '2026-12-05', '시간': '14:00'}";
  const 예약 = JSON.parse(저장된글);
  결과보여주기(`예약: ${예약.날짜} ${예약.시간}`);
});
