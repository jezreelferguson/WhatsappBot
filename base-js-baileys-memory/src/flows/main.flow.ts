import axios from "axios";

export default async function flow(ctx, { flowDynamic }) {
    const userMessage = ctx.body;
    const phone = ctx.from;

    try {
        const res = await axios.post("http://localhost:8000/chat", {
            phone,
            message: userMessage
        });

        await flowDynamic(res.data.reply);

    } catch (err) {
        await flowDynamic("Error connecting to AI server.");
    }
}