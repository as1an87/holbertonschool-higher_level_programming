-- Find the state_id for California using a subquery

SELECT `id`, `name` FROM `cities` WHERE `state_id` IN
(SELECT `id` FROM `states` WHERE `name` = "California") ORDER BY `id`;
