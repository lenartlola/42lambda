import {nanoid} from "nanoid";
import {useEffect, useState} from "react";
import Link from "next/link";

export default function AuthHandshake() {
    const auth = `https://api.intra.42.fr/oauth/authorize?client_id=` + process.env.CLIENT_ID + "&redirect_uri=" +process.env.REDIRECT_URI + "&scope=public" + "&state=code=" + nanoid() + "&response_type=code";
    return (
        <div>
            <Link href={auth}>LOGIN</Link>
        </div>
    )
}