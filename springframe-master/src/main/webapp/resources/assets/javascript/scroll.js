/**
 * Created by gohyunyoung98 on 16. 7. 25.
 */

$(document).ready(function() {
    // Each time the user scrolls
    $(window).scroll(function() {
        // End of the document reached?
        if ($(document).height() - $(window).height() == $(window).scrollTop()) {
            var articleId = $('li.timeline:nth-last-of-type(2)').attr('id');
            var sequence="DESC";
            // RECENT->OLD 순서
            // console.log($('li.timeline:nth-last-of-type(3)').attr('id'));
            // console.log($('li.timeline:nth-last-of-type(2)').attr('id').val());
            if(parseInt($('li.timeline:nth-last-of-type(3)').attr('id'))<parseInt($('li.timeline:nth-last-of-type(2)').attr('id'))){
                // ASC = OLD->RECENT 순서(오름차순)
                sequence="ASC";
                articleId ++;
            }
            else{
                // DESC = RECENT -> OLD 순서
                sequence="DESC";
                articleId--;
            }
            // ajax로 넘겨줄 parameter
            var param = {"articleId":articleId,"sequence":sequence};

            $.ajax({
                url: '/scroll',
                type: 'get',
                data: param,
                success: function (data) {
                    // console.log('success 전 : '+ param.articleId);
                    // console.log($('li.timeline:nth-last-of-type(2)').attr('id'));
                    // if(param.sequence=="DESC")
                    //     articleId=$('li.timeline:nth-last-of-type(2)').attr('id')-1;
                    // else
                    //     param.articleId=$('li.timeline:nth-last-of-type(2)').attr('id')+1;
                    // console.log('success 후 : '+ param.articleId);
                    // console.log("articleId = "+articleId);
                    console.log("sequence = "+sequence);
                    // console.log("param.articleId = "+param.articleId);
                    // console.log("param.sequence = "+param.sequence);

                    // console.log(data);
                    $('li#getMoreArticle').before(data);
                },
                error : function () {
                    console.log("error");
                }
            });
        }
    });
});