$(()=>{
    function callApi(type) {
        let params = {
            q : $("#text").val(),
            type : type,
        };
        let url = "/?" + $.param(params);
        $.get(url, (data)=>{
            $("#output").text(data);
        });
    }
    
    $("#btn_wrap").on("click", "button", (e)=>{
        callApi(e.target.id);
    });
});