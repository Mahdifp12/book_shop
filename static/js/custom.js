function sendArticleComment() {

    var comment = $("#comment-text-article").val();

    $.get("/articles/add-article-comment", {
        ArticleComment : comment,
        ArticleId : 9,
        ArticleParent : null
    }).then(res => {
        console.log(res);
    });
}