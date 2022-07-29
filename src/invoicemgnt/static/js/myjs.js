$(document).ready(function(){
  
 // alert("We are all set!");

 $('#id_line_one_chequier, #id_line_one_P_U,#id_line_two_chequier, #id_line_two_P_U,#id_line_two_P_V_HTVA,#id_line_two_T_V_A,#id_line_two_P_V_TVAC').keyup(function(){
    
    var line_one_chequier_text = Number($('#id_line_one_chequier').val());
    var line_one_P_U_text = $('#id_line_one_P_U').val();
     

    var line_one_HTVA_text = line_one_chequier_text * line_one_P_U_text
    var line_one_TVA_text = line_one_HTVA_text * 0.18
    var line_one_TVAC_text = line_one_HTVA_text + line_one_TVA_text

      $('#id_line_one_P_V_HTVA').val(line_one_HTVA_text);
      $('#id_line_one_T_V_A').val(line_one_TVA_text);
      $('#id_line_one_P_V_TVAC').val(line_one_TVAC_text);

    var line_two_chequier_text = Number($('#id_line_two_chequier').val());
    var line_two_P_U_text = $('#id_line_two_P_U').val();
     

    var line_two_HTVA_text = line_two_chequier_text * line_two_P_U_text
    var line_two_TVA_text = line_two_HTVA_text * 0.18
    var line_two_TVAC_text = line_two_HTVA_text + line_two_TVA_text

    $('#id_line_two_P_V_HTVA').val(line_two_HTVA_text);
    $('#id_line_two_T_V_A').val(line_two_TVA_text);
    $('#id_line_two_P_V_TVAC').val(line_two_TVAC_text);

    var total_htva = line_one_HTVA_text + line_two_HTVA_text
    var total_tva = line_one_TVA_text+ line_two_TVA_text
    var total_tvac = line_one_TVAC_text + line_two_TVAC_text
    var total_check = line_one_chequier_text + line_two_chequier_text

    $('#id_total_HTVA').val(total_htva);
    $('#id_total_TVA').val(total_tva);
    $('#id_total_TVAC').val(total_tvac);
    $('#id_Quantity_check').val(total_check);
    
});


});