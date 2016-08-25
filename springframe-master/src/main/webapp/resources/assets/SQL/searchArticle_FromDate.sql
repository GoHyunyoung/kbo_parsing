Drop procedure if exists Article.searchArticle_FromDate;
Delimiter $$
create procedure searchArticle_FromDate(searchDate char(8))
Begin
set @searchDateMinId = (select min(Article.id) from Article where date like concat(searchDate,'%'));
SELECT 
    *
FROM
    Article
WHERE
    id >= @searchDateMinId;
end $$