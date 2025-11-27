document.addEventListener("DOMContentLoaded", function() {

    const stateSelect = document.getElementById("stateSelect");
    const districtSelect = document.getElementById("districtSelect");

    stateSelect.addEventListener("change", function() {

        const state = stateSelect.value;
        if (!state) return;

        fetch(`/get_districts/${state}`)
            .then(res => res.json())
            .then(data => {
                districtSelect.innerHTML = "";
                data.districts.forEach(d => {
                    let op = document.createElement("option");
                    op.value = d;
                    op.innerText = d;
                    districtSelect.appendChild(op);
                });
            });
    });

});
