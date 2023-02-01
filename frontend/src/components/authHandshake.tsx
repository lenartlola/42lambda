import {nanoid} from "nanoid";
import Link from "next/link";
import * as process from "process";

export default function AuthHandshake() {
    let client_id = process.env.CLIENT_ID;
    let redirect_uri = process.env.REDIRECT_URI;
    let scope = "public";
    let state = nanoid();
    let response_type = "code";
    return (
        <div>
            <Link href={`https://api.intra.42.fr/oauth/authorize?client_id=${client_id}&redirect_uri=${redirect_uri}&scope=${scope}&state=${state}&response_type=${response_type}`}>LogIN</Link>
        </div>
    )
}