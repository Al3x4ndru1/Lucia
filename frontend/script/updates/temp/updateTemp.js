export default function (TempValue) {
	const TempValue1 = document.querySelector('.TempValue1');

	TempValue1.textContent = `${TempValue}°C`;
	console.log(TempValue);
}