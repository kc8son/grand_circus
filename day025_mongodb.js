//	Joe Merten - Homework assignment - People Pt.1 (MongoDB Queries)

List all people. (200)
db.people.find()

Count all people. (200)
db.people.find().count()

List all people in Arizona. (6)
db.people.find({ state: { $eq: 'Arizona' } })

List all males in Arizona. (2)
db.people.find( 
    {$and: [
		{ state: { $eq: 'Arizona' } },
		{ gender: { $eq: 'Male' } }
	] }
)

List all people in Arizona plus New Mexico. (8)
db.people.find( 
    {$or: [
		{ state: { $eq: 'Arizona' } },
		{ state: { $eq: 'New Mexico' } }
	] }
)


List all people under age 40. (90)
db.people.find({ age: { $lt: 40 } })

List all females in Florida between the ages of 40 and 45 (inclusive). (4)
db.people.find( 
    {$and: [
		{ state: { $eq: 'Florida' } },
		{ age: { $gte: 40 } },
		{ age: { $lte: 45 } },
		{ gender: { $eq: 'Female' } }
	] }
)


List people whose first name starts with "H". (2)
db.people.find( 
    { first_name: /^H/}
)

List all people in Michigan, sorted by first name. (6)
db.people.find({ state: { $eq: 'Michigan' } }).sort({"first_name":1})


List all people who live in Virginia or are named Virginia.
db.people.find( 
    {$or: [
		{ state: { $eq: 'Virginia' } },
		{ first_name: { $eq: 'Virginia' } }
	] }
)


List the names of people under age 30. Only display their first and last name. (38)
db.people.find( 
    { age: { $lt: 30} },
	{ first_name: true, last_name: true }
)


List all people in Montana. Display all information except age. (2)
db.people.find( 
    { state: { $eq: 'Montana' }},
	{ age: false }
)


List the email addresses of people with a ".edu" email. Only display the email. (12)
db.people.find( 
    { email: /.edu$/},
	{ email: true}
)


Extended Challenges:
========================
Count all people with at least one child under age four. (69)
////	This is the hardrst of the three!!
////	From this article: https://stackoverflow.com/questions/23553922/mongodb-find-inside-sub-array
db.people.find({
   children:{
      $elemMatch:{
         age:{
            $lt:4
         }
      }
   }
})

List people who have no children. (43)
db.people.find( 
	{ children: { $exists: true, $size: 0} }
)
/////  $exists doesn't work since there's an empty list
db.people.find( 
	{ children: { $exists: false}}
)


List people who have at least one child. (157)
db.people.find( 
	{ children: { $exists: true, $not: {$size: 0} } })






	---notes---
"^xxx" - begins with
"xxx$" - ends with

{ $match: { language: { $exists: true}}}


db.collection1.find({ age: { $gt: 30 } }).forEach(function(doc) {
  db.collection2.insert(doc);
});


db.collection1.find({ age: { $gt: 30 } }).forEach(function(doc) {
  db.collection2.insert(doc);
});

