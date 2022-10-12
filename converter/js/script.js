const weightOptions = [
    {id: 1, value: "kilogram"},
    {id: 2, value: "gram"},
    {id: 3, value: "milligram"},
    {id: 4, value: "stone"},
    {id: 5, value: "pound"},
    {id: 6, value: "ounce"},
    {id: 7, value: "pud"},
    {id: 8, value: "grivna"},
    {id: 9, value: "lot"}
]

const lengthOptions = [
    {id: 1, value: "kilometer"},
    {id: 2, value: "meter"},
    {id: 3, value: "centimeter"},
    {id: 4, value: "mile"},
    {id: 5, value: "foot"},
    {id: 6, value: "inch"},
    {id: 7, value: "versta"},
    {id: 8, value: "sazhen"},
    {id: 9, value: "arshin"}
]

const temperatureOptions = [
    {id: 1, value: "kelvin"},
    {id: 2, value: "celsius"},
    {id: 3, value: "fahrenheit"},
    {id: 4, value: "reaumur"}
]

const speedOptions = [
    {id: 1, value: "kilometer_per_hour"},
    {id: 2, value: "meter_per_second"},
    {id: 3, value: "mile_per_hour"},
    {id: 4, value: "foot_per_second"}
]

const main_select = document.getElementById('main_select')
const left_select = document.getElementById('left_select')
const right_select = document.getElementById('right_select')
const convertBtn = document.getElementById('convert_btn')
const input = document.getElementById('input')
const output = document.getElementById('output')

function removeOptions(selectElement) {
    let i, L = selectElement.options.length - 1;
    for (i = L; i >= 0; i--) {
        selectElement.remove(i);
    }
}

function fillOptions(selectElement, optionsArray) {
    let length = optionsArray.length
    for (let i = 0; i < length; i++) {
        let option = document.createElement('option')
        option.setAttribute('value', '')
        option.appendChild(document.createTextNode(optionsArray[i].value))
        selectElement.appendChild(option)
    }
}

const selectHandler = (selectElement, optionsArray) => {
    removeOptions(selectElement)
    fillOptions(selectElement, optionsArray)
}

main_select.addEventListener('change', (e) => {
    let chosenOption = main_select.options[main_select.selectedIndex].text
    switch (chosenOption) {
        case 'weight':
            selectHandler(left_select, weightOptions)
            selectHandler(right_select, weightOptions)
            break
        case 'length':
            selectHandler(left_select, lengthOptions)
            selectHandler(right_select, lengthOptions)
            break
        case 'speed':
            selectHandler(left_select, speedOptions)
            selectHandler(right_select, speedOptions)
            break
        case 'temperature':
            selectHandler(left_select, temperatureOptions)
            selectHandler(right_select, temperatureOptions)
            break
    }
})
let text = ""
async function fetchAsync(url) {
    console.log(url)
    text = await fetch(url).then((response) => response.json()).then((e) => {
        return e
    });
    output.innerText = text
}

convertBtn.addEventListener('click', (e) => {
    fetchAsync(`http://localhost:5000/convert/${input.value}/${main_select[main_select.options.selectedIndex].text}/${left_select[left_select.options.selectedIndex].text}/${right_select[right_select.options.selectedIndex].text}`);
})