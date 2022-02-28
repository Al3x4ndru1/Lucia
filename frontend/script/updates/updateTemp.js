export default function (TempValue) {
	const TempValue = document.querySelector('.TempValue').value;

	TempValue.textContent = `${TempValue}°C`;
}