import axios from "axios"; // 前后端的连接

// const API = axios.create({
//   baseURL: "http://127.0.0.1:8000",
// });
const API = axios.create({
  baseURL: "https://auto-grader-web-app.onrender.com/",
});

// 对应后端的两个endpoints
export const submitCode = async (code) => {
  const res = await API.post("/grade", { code });
  return res.data;
};

export const uploadFile = async (file) => {
  const form = new FormData();
  form.append("file", file);
  const res = await API.post("/upload", form, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return res.data;
};
