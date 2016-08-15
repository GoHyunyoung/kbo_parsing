/**
 * Created by gohyunyoung98 on 16. 7. 25.
 */

$(document).ready(function () {
    var win = $(window);
    var articleId = $('li.timeline:nth-last-of-type(2)').attr('id')-1;
    var sequence="DESC";
    // RECENT->OLD 순서
    if($('li.timeline:nth-last-of-type(3)').attr('id')<$('li.timeline:nth-last-of-type(2)').attr('id')){
        // ASC = OLD->RECENT 순서(오름차순)
        sequence="ASC";
    }
    else{
        // DESC = RECENT -> OLD 순서
        sequence="DESC";
    }

    // ajax로 넘겨줄 parameter
    var param = {"articleId":articleId,"sequence":sequence};

    // Each time the user scrolls
    win.scroll(function () {
        // End of the document reached?
        if ($(document).height() - win.height() <= win.scrollTop()) {
            $.ajax({
                url: '/scroll',
                type: 'get',
                data: param,
                success: function (data) {
                    console.log('success 전 : '+articleId);
                    console.log($('li.timeline:nth-last-of-type(2)').attr('id'));
                    if(sequence=="DESC")
                        articleId=$('li.timeline:nth-last-of-type(2)').attr('id')-1;
                    else
                        articleId=$('li.timeline:nth-last-of-type(2)').attr('id')+1;
                    console.log($('li.timeline:nth-last-of-type(2)').attr('id'));
                    console.log('success 후 : '+articleId);
                    $('li#getMoreArticle').before(data);
                },
                error : function () {
                  console.log("error");
                }
            });
        }
    });
});