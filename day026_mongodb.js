//	Joe Merten - Homework assignment - People Pt.2 (MongoDB Queries)

In people collection
=======================
 1 - Add a person to the collection. You pick the data, but they should have an empty array for children.
 db.people.insert(
	{
	  first_name: 'Worowak',
	  last_name: 'Sapawak',
	  email: 'WS@nowhere.com',
	  gender: 'Male',
	  age: 45,
	  state: 'Bangkok',
	  children: []
	}
)


 2 - Add another person. They should have at least two children.
 db.people.insert(
	{
	  first_name: 'Joe',
	  last_name: 'Schmoe',
	  email: 'JSchmoe@nowhere.com',
	  gender: 'Male',
	  age: 59,
	  state: 'Minnesota',
	  children: [
	    {
	      name: 'Anne',
	      age: 11
	    },
	    {
	      name: 'Beth',
	      age: 15
	    },
	    {
	      name: 'Charlie',
	      age: 17
	    }
	  ]
	}
)

 3 - Update one person named Clarence. He moved from North Dakota to South Dakota.
 db.people.find(
 	{first_name: 'Clarence'}
 )
db.people.updateOne(
   {first_name: 'Clarence'},
   {
     $set: { "state": "South Dakota" }
   }
)

 db.people.find(
 	{first_name: 'Clarence'}
 )


 4 - Update Rebecca Hayes. Remove her email address.
=======
 db.people.insertOne(
	{  first_name: 'Tim',
	  last_name: 'Adams',
	  email: 'whome@nowhere.cn',
	  gender: 'Male',
	  age: 22,
	  state: 'Minnesota',
	  children: []
	}
 )
 //Confirm:
 db.people.find({email: 'whome@nowhere.cn'})
 
 2 - Add another person. They should have at least two children.
 db.people.insertOne(
	{  first_name: 'Mary',
	  last_name: 'Jones',
	  email: 'mjones@nowhere.com',
	  gender: 'female',
	  age: 30,
	  state: 'Minnesota',
	  children: [
		{
		  name: 'Thing 2',
		  age: 1
		},
		{
		  name: 'Thing 1',
		  age: 3
		}
	]
	}
 )
 //Confirm:
 db.people.find({email: 'mjones@nowhere.com'})

 3 - Update one person named Clarence. He moved from North Dakota to South Dakota.
 db.people.updateOne(
	{first_name: 'Clarence'},
	{
		$set: {state: 'South Dakota'}
	}
 )
 //Confirm:
 db.people.find({first_name: 'Clarence'})


 4 - Update Rebecca Hayes. Remove her email address.
 db.people.updateOne(
 	{$and: [
		{first_name: 'Rebecca'},
		{last_name: 'Hayes'}
	] },
	{
		$unset: {email: ''}
	}
 )
 //Confirm:
 db.people.find(
	{$and: [
		{first_name: 'Rebecca'},
		{last_name: 'Hayes'}
	] }
)


 5 - Update everyone from Missouri. They all had a birthday today, so add one to their age. (expect 4 matches)
db.people.updateMany(
	{state: 'Missouri'},
	{ $inc: { age: 1 } }
)
 //Confirm: 47, 60, 51, 29 before....
 db.people.find(
	{state: 'Missouri'},
	{first_name: 1, last_name: 1, age: 1}
)
// After 48, 61, 52, 30

 6 - Jerry Baker has updated information. Replace with a new document:
{ first_name: "Jerry", last_name: "Baker-Mendez", email: "jerry@classic.ly", gender:"Male", age: 28, state: "Vermont", "children": [{name: "Alan", age: 18}, {name: "Jenny", age: 3}] }
//	pre update:
 db.people.find(
	{$and: [
		{first_name: 'Jerry'},
		{last_name: 'Baker'}
	] }
)
db.people.replaceOne(
	{$and: [
		{first_name: 'Jerry'},
		{last_name: 'Baker'}
	] }, 
	{ first_name: "Jerry", last_name: "Baker-Mendez", email: "jerry@classic.ly", gender:"Male", age: 28, state: "Vermont", "children": [{name: "Alan", age: 18}, {name: "Jenny", age: 3}] }
)
//	post update check 1 = equals zero documents
 db.people.find(
	{$and: [
		{first_name: 'Jerry'},
		{last_name: 'Baker'}
	] }
).count()
//	post update check 2 = equals one document
 db.people.find(
	{$and: [
		{first_name: 'Jerry'},
		{last_name: 'Baker-Mendez'}
	] }
).count()

 7 - Delete Wanda Bowman.
//	pre update:
 db.people.find(
	{$and: [
		{first_name: 'Wanda'},
		{last_name: 'Bowman'}
	] }
)

db.people.remove(
	{$and: [
		{first_name: 'Wanda'},
		{last_name: 'Bowman'}
	] }
)

//	post update:  Yup, she's gone ;-)
 db.people.find(
	{$and: [
		{first_name: 'Wanda'},
		{last_name: 'Bowman'}
	] }
)

 8 - Delete everyone who does not have an email address specified. (expect 36 matches - maybe more depending what you added above)
//	pre update #1 - This only count 1 document:
 db.people.find(
		{ "email" : { "$exists" : false } }
).count()
//	pre update #2 - This also only count 1 document:
 db.people.find(
		{ "email" : { "$exists" : null } }
).count()
//	pre update #3 - There are 203 documents...
db.people.find().count()
//	First delete...  deletedCount: 1
db.people.deleteMany(
		{ "email" : { "$exists" : false } }
)
//	Apparrently that was the same document, there are no documents that match 
//  { "email" : { "$exists" : null } }
//  202 documents left.
db.people.find(
		{ "email" : { "$exists" : null } }
).count()




In submissions collection
=============================
 9 - Add several documents to a new submissions collection. Do it all in one command. (Remember, MongoDB will create the collection for you. Just start adding documents.)
     a - title: "The River Bend", upvotes: 10, downvotes: 2, artist: <ID of Anna Howard>
     b - title: "Nine Lives", upvotes: 7, downvotes: 0, artist: <ID of Scott Henderson>
     c - title: "Star Bright", upvotes: 19, downvotes: 3, artist: <ID of Andrea Burke>
     d - title: "Why Like This?", upvotes: 1, downvotes: 5, artist: <ID of Steven Marshall>
     e - title: "Non Sequitur", upvotes: 11, downvotes: 1, artist: <ID of Gerald Bailey>
 db.people.find(
	{$and: [
		{first_name: 'Anna'},
		{last_name: 'Howard'}
	] }
)
//  https://www.mongodb.com/community/forums/t/insert-values-from-one-collection-to-fields-in-another-collection/156403
//  https://groups.google.com/g/mongodb-user/c/X9UltGPVpnw/m/z9LVo7s8CQAJ?pli=1

db.submissions.insertMany( [
	{ title: "The River Bend", upvotes: 10, downvotes: 2, artist:  ObjectId("6449cfdfd35f4bff0d3c4efb") },
	{ title: "Nine Lives", upvotes: 7, downvotes: 0, artist: ObjectId("6449cfdfd35f4bff0d3c4f29") }, 
	{ title: "Star Bright", upvotes: 19, downvotes: 3, artist: ObjectId("6449cfdfd35f4bff0d3c4fac") }, 
	{ title: "Why Like This?", upvotes: 1, downvotes: 5, artist: ObjectId("6449cfdfd35f4bff0d3c4f32") }, 
	{ title: "Non Sequitur", upvotes: 11, downvotes: 1, artist: ObjectId("6449cfdfd35f4bff0d3c4ef9") }
] )

10 - Add 2 upvotes for "The River Bend".
//	 pre-update = 10 upvotes...
db.submissions.find(
	{ title: "The River Bend"}
)
//	Do the update...
db.submissions.updateOne(
   { title: "The River Bend" },
   { $inc: { upvotes: +2 } }
)
//	 pre-update = 12 upvotes...
db.submissions.find(
	{ title: "The River Bend"}
)



11 - Add a field round2 = true to all submissions with at least 10 upvotes. (expect 3 matches)
//	 pre-update = found three...
db.submissions.find(
	{ upvotes: { $gt: 10 } }
)
//	Do the update...  
//	 matchedCount: 3,
//	 modifiedCount: 3,
db.submissions.updateMany(
   { upvotes: { $gt: 10 } },
   { $push: { round2: true } }
)
//	Post update...  This worked, but appears to have added it as an array/list
db.submissions.find(
	{ upvotes: { $gt: 10 } }
=======
 1 - Add a person to the collection. You pick the data, but they should have an empty array for children.
 db.people.insert(
	{
	  first_name: 'Worowak',
	  last_name: 'Sapawak',
	  email: 'WS@nowhere.com',
	  gender: 'Male',
	  age: 45,
	  state: 'Bangkok',
	  children: []
	}
)


 2 - Add another person. They should have at least two children.
 db.people.insert(
	{
	  first_name: 'Joe',
	  last_name: 'Schmoe',
	  email: 'JSchmoe@nowhere.com',
	  gender: 'Male',
	  age: 59,
	  state: 'Minnesota',
	  children: [
	    {
	      name: 'Anne',
	      age: 11
	    },
	    {
	      name: 'Beth',
	      age: 15
	    },
	    {
	      name: 'Charlie',
	      age: 17
	    }
	  ]
	}
)

 3 - Update one person named Clarence. He moved from North Dakota to South Dakota.
 db.people.find(
 	{first_name: 'Clarence'}
 )
db.people.updateOne(
   {first_name: 'Clarence'},
   {
     $set: { "state": "South Dakota" }
   }
)

 db.people.find(
 	{first_name: 'Clarence'}
 )


 4 - Update Rebecca Hayes. Remove her email address.
////	There is only one row with a first nme of rebecca, I don't need the last name.
 db.people.find(
 	{$and [
 		{first_name: 'Rebecca'},
 		{last_name: 'Hayes'}
 	] }
 )
db.people.updateOne(
   {first_name: 'Rebecca'},
   {
     $set: { "state": "South Dakota" }
   }
)

 db.people.find(
 	{first_name: 'Rebecca'}
 )


Extended Challenges:
12 - Update Helen Clark. She had a baby! Add a child, name: Melanie, age: 0.
13 - Joan Bishop has a child named Catherine. She just had a birthday and prefers to go by "Cat". In one query update the child's name to "Cat" and increment her age by one.
14 - List all submissions that have more downvotes than upvotes.







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
=====================
12 - Update Helen Clark. She had a baby! Add a child, name: Melanie, age: 0.


13 - Joan Bishop has a child named Catherine. She just had a birthday and prefers to go by "Cat". In one query update the child's name to "Cat" and increment her age by one.


14 - List all submissions that have more downvotes than upvotes.


// mongodb+srv://kc8son:xafl8iLm6IGXVMBZ@cluster0.utmyy3i.mongodb.net/test
===============================
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
