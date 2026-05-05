export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, PUT, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") return res.status(200).end();

  const GH_TOKEN = process.env.GH_TOKEN;
  const GH_OWNER = process.env.GH_OWNER;
  const GH_REPO = process.env.GH_REPO;
  const GH_FILE = process.env.GH_FILE || "leaderboard.json";
  const GH_BRANCH = process.env.GH_BRANCH || "main";
  const GH_API = `https://api.github.com/repos/${GH_OWNER}/${GH_REPO}/contents/${GH_FILE}`;

  const ghHeaders = {
    Authorization: `token ${GH_TOKEN}`,
    Accept: "application/vnd.github.v3+json",
    "Content-Type": "application/json",
  };

  if (req.method === "GET") {
    const r = await fetch(`${GH_API}?ref=${GH_BRANCH}&t=${Date.now()}`, {
      headers: ghHeaders,
    });
    const data = await r.json();
    return res.status(r.status).json(data);
  }

  if (req.method === "PUT") {
    const r = await fetch(GH_API, {
      method: "PUT",
      headers: ghHeaders,
      body: JSON.stringify(req.body),
    });
    const data = await r.json();
    return res.status(r.status).json(data);
  }

  res.status(405).json({ error: "Method not allowed" });
}
