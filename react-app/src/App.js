import { useEffect, useState } from 'react';

function App() {
  const [content, setContent] = useState("");
  const [message, setMessage] = useState("");
  const [msgs, setMsgs] = useState([]);
  const [user, setUser] = useState("noname");
  const [pnum, setPnum] = useState(1);
  const [plast, setplast] = useState(1);

  const getMsgs = (num) => {
    getPlast();
    setPnum(num);
    fetch("http://localhost:8000/api/msgs/" + num)
      .then(resp => resp.json())
    .then(res => {
      setMsgs(res);
    });
  }

  const getUser = () => {
    fetch("api/usr")
      .then(resp => resp.json())
    .then(res => {
      setPlast(res.value);
    });
  }

  const doChange = (event) => {
    setContent(event.target.value);
  }
  const doAction = (event) => {
    const data = {
      content:content,
    }
    fetch("/api/post", {
      method: "post",
      headers: {},
      body: JSON.stringify(data),
    }).then(resp => resp.text())
        .then(res => {
          getPlast();
          getMsgs(1);
          if (res == "OK") {
            setContent("");
            setMessage("メッセージを投稿しました！");
          }
        });
  }

  const doGood = (event) => {
    fetch("/api/good" + event.target.id)
      .then(resp => resp.text())
        .then(res => {
          getMsgs(pnum);
          if (res == "OK") {
            setMessage("Good!しました。");
          } else {
            setMessage("既にGoodしています。");
          }
        });
    }

    const onFirst = (event) => {
      getMsgs(1);
    }

    const onPrev = (event) => {
      const p = pnum-1 <= 1 ? 1 : pnum-1;
      getMsgs(p)
    }

    const onNext = (event) => {
      const p = pnum+1 <= 1 ? 1 : pnum+1;
      getMsgs(p)
    }

    const onLast = (event) => {
      getMsgs(plast);
    }

    useEffect(()=>{
      getUser();
      getMsgs(1);
    }, []);

    return(
      <></>
    );
  };

export default App;
