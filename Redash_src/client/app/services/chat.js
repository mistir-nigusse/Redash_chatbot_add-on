import { axios } from "@/services/axios";
   
const Chat = {
  openai: data => axios.post('api/chat', data),
};

export default Chat;