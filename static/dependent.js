document.addEventListener("DOMContentLoaded", function() {

    const stateSelect = document.getElementById("stateSelect");
    const districtSelect = document.getElementById("districtSelect");

    // Add event listener to the State dropdown
    stateSelect.addEventListener("change", function() {

        const state = stateSelect.value;
        // Clear old districts
        districtSelect.innerHTML = '<option value="">Loading Districts...</option>';
        districtSelect.disabled = true;

        if (!state) {
            districtSelect.innerHTML = '<option value="">Select State First</option>';
            districtSelect.disabled = false;
            return;
        }

        // Fetch districts from the Flask route
        fetch(`/get_districts/${encodeURIComponent(state)}`)
            .then(res => res.json())
            .then(data => {
                districtSelect.innerHTML = "";
                districtSelect.disabled = false;

                if (data.districts && data.districts.length > 0) {
                    // Add a default placeholder option
                    districtSelect.innerHTML = '<option value="">-- Select District --</option>';

                    // Populate with new districts
                    data.districts.forEach(d => {
                        let op = document.createElement("option");
                        op.value = d;
                        op.innerText = d;
                        districtSelect.appendChild(op);
                    });
                } else {
                    districtSelect.innerHTML = '<option value="">No districts found</option>';
                }
            })
            .catch(error => {
                console.error("Error fetching districts:", error);
                districtSelect.innerHTML = '<option value="">Error loading</option>';
                districtSelect.disabled = false;
            });
    });

});