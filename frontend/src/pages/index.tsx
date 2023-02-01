import Head from 'next/head'
import { Inter } from '@next/font/google'
import AuthHandshake from "@/components/authHandshake";

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
      <Head>
        <title>42lambda</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <AuthHandshake></AuthHandshake>
    </>
  )
}