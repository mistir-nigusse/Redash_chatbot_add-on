import React,{ useState} from 'react'
import redashpng from "@/assets/images/favicon-96x96.png";
import './chatbox.less'
import Chat from '@/services/chat';
import { IoCopy } from "react-icons/io5";
import { FaCheck } from "react-icons/fa6";
import SyntaxHighlighter from 'react-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/dist/esm/styles/hljs';
import copy from 'copy-to-clipboard';


export default function ChatBox() {
  const [input, setInput] = useState("")
  const [open, setOpen] = useState(false);
  const [copiedStates, setCopiedStates] = useState({});
  const [chatHistory, setChatHistory] = useState([]);

  const handler = (event) => {
    if (event.keyCode === 13) {      
      handleChatInput();
    }
  };

  function handleChatInput() {
    const data = { sender: "user", text: input };
    if (input !== "") {
      setChatHistory((history) => [...history, data]);
      chatWithOpenai(input);    
      setInput("");  
    }
  }

  async function chatWithOpenai(text) {
    const requestOptions = {
        question: text
    };
    const response = await Chat.openai(requestOptions);
    const data = {
      sender: "bot",
      text: response.answer
    };
     setChatHistory((history) => [...history, data]);
     setInput("");
  }

  const handleCopy = (content) => {
    copy(content);
    const updatedCopiedStates = { ...copiedStates };
    updatedCopiedStates[content] = true;
    setCopiedStates(updatedCopiedStates);

    setTimeout(() => {
      const revertedCopiedStates = { ...copiedStates };
      revertedCopiedStates[content] = false;
      setCopiedStates(revertedCopiedStates);
    }, 2000); // Change the duration (in milliseconds) as needed
  };

  const formatingCode = (code) => {
    // Split the code by lines to remove unnecessary white spaces
    const lines = code.split(/\s*(?=<)/);
    
    // Remove leading and trailing white spaces from each line
    const trimmedLines = lines.map((line) => line.trim());
    
    // Join the lines with line breaks and indentation
    const formattedCode = trimmedLines.join('\n');
    
    return formattedCode;
  };

  const splitAnswerParts = (answer) => {
    const parts = [];
    const codeRegex = /```([\s\S]*?)```/g;
  
    let match;
    let lastIndex = 0;
  
    while ((match = codeRegex.exec(answer))) {
      const codeContent = match[1].trim();
  
      if (match.index > lastIndex) {
        const textContent = answer.substring(lastIndex, match.index).trim();
        parts.push({ type: 'text', content: textContent });
      }
  
      const lines = codeContent.split('\n');
      const firstLine = lines[0].trim();
      const firstWord = firstLine.split(' ')[0];
      const firstLineEndIndex = codeContent.indexOf(' ') + 1;
      const remainingCode = codeContent.substring(firstLineEndIndex).trim();
      const formattedCodeContent = formatingCode(remainingCode); // Process the remaining code through formatingCode function
  
      parts.push({ type: 'code', firstWord, content: formattedCodeContent });
  
      lastIndex = match.index + match[0].length;
    }
  
    if (lastIndex < answer.length) {
      const textContent = answer.substring(lastIndex).trim();
      parts.push({ type: 'text', content: textContent });
    }
  
    return parts;
  };

  
  return (
    <>
      {open?
      <div className='chatcontainer'>
        <div>
            <div className='headbox'>
              <p>query, visualize with AI</p>            
            </div>

            <div className='chatbox'>
              {chatHistory.map((chat, index) => (
                <div key={index} className="chatcontain">
                  {chat.sender === "user" ? (
                    <div className="user">
                      <div className="">
                        <p className="parauser">{chat?.text}</p>
                      </div>
                    </div>
                  ) : (
                    <div className='ai'>
                      <div className="">
                        {chat?.text && (
                          <div>
                            {splitAnswerParts(chat.text).map((part, partIndex) => (
                              <React.Fragment key={partIndex}>
                                {part.type === 'code' ? (
                                  <div className="">
                                    <div className='chat-head'>
                                        <div className='copy' onClick={() => handleCopy(part.content)}>
                                          {copiedStates[part.content] ? (
                                            <FaCheck className='check'/>
                                          ) : (
                                            <IoCopy className='copyicon'/>
                                          )}
                                        </div>
                                        <div className=''>
                                          {part.firstWord}
                                        </div>                            
                                    </div>
                                    <SyntaxHighlighter
                                      language={part.firstWord}
                                      style={docco}
                                      className='x-container'
                                      customStyle={{
                                        fontSize: '14px',
                                        lineHeight: '1.5',
                                        maxWidth: '100%',
                                        wordBreak: 'break-word',
                                        overflowWrap: 'break-word',
                                        whiteSpace: 'pre-wrap',
                                        overflow: 'auto'
                                      }}
                                    >
                                      {part.content}
                                    </SyntaxHighlighter>
                                  </div>
                                ) : (
                                  <p>{part.content}</p>
                                )}
                              </React.Fragment>
                            ))}
                          </div>
                        )}
                      </div>
                    </div>
                  )}
                </div>
              ))}
            </div>

            <div className='inputbox'>        
              <input             
                  className="input"    
                  type="text"
                  value={input}
                  placeholder="Type your message…"
                  onChange={(e) => setInput(e.target.value)}
                  onKeyDown={(e) => handler(e)}
              />
            </div>
        </div>
      </div>
      :null}

      <div className='iconbox' onClick={()=>setOpen(!open)}>
         <img alt="charimage" src={redashpng} className="icon" />
      </div>     
    </>
  )
}