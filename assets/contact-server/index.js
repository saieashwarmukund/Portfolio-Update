const express = require('express');
const sgMail = require('@sendgrid/mail');
const dotenv = require('dotenv');

dotenv.config();
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

const app = express();
app.use(express.json());
console.log('hi');
app.use(express.urlencoded({ extended: true }));

app.post('/contact', async (req, res) => {
    const { name, email, subject, message } = req.body;

    const msg = {
        to: 'saieashwar@gmail.com', // Your email
        from: email, // Sender's email
        subject: `New Contact Form Submission: ${subject}`,
        text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}`
    };

    console.log('poopy butt');

    try {
        await sgMail.send(msg);
        res.status(200).send('Email sent successfully!');
    } catch (error) {
        console.error(error);
        res.status(500).send('Failed to send email.');
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
