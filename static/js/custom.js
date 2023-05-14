function sendArticleComment(articleId) {

    var comment = $("#comment-text-article").val();
    var parentId = $("#parent_id").val();

    $.get("/articles/add-article-comment", {
        article_comment : comment,
        article_id : articleId,
        parent_id : parentId
    }).then(res => {
        $('#comments_area').html(res);
        $('#comment-text-article').val('');
        $('#parent_id').val('');
        document.getElementById('comments_area').scrollIntoView({behavior: "smooth"});
        if (parentId !== null && parentId !== ''){
            document.getElementById('singel_comment_box_' + parentId).scrollIntoView({behavior: "smooth"});
        }else{
            document.getElementById('comments_area').scrollIntoView({behavior: "smooth"});
        }
    });
}

function fillParentId(parentId){
    $("#parent_id").val(parentId)
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}