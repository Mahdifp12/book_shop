function sendArticleComment(articleId) {

    var comment = $("#comment-text-article").val();
    var parentId = $("#parent_id").val();

    $.get("/articles/add-article-comment", {
        article_comment : comment,
        article_id : articleId,
        parent_id : parentId
    }).then(res => {
        console.log(res);
    });
}

function fillParentId(parentId){
    $("#parent_id").val(parentId)
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}