import React, { useEffect, useState } from 'react';

function App() {
  const [content, setContent] = useState("");
  const [message, setMessage] = useState("");
  const [msgs, setMsgs] = useState([]);
  const [user, setUser] = useState("noname");
  const [pnum, setPnum] = useState(1);
  const [plast, setPlast] = useState(1);

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
    fetch("/api/usr")
      .then(resp => resp.json())
      .then(res => {
        setUser(res.value);
      });
  }

  const getPlast = () => {
    fetch("/api/plast")
      .then(res => {
        setPlast(res.value);
      });
  }

  const doChange = (event) => {
    setContent(event.target.value);
  }
  const doAction = (event) => {
    const data = {
      content: content,
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
    fetch("/api/good/" + event.target.id)
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
    const p = pnum - 1 <= 1 ? 1 : pnum - 1;
    getMsgs(p)
  }

  const onNext = (event) => {
    const p = pnum + 1 <= 1 ? 1 : pnum + 1;
    getMsgs(p)
  }

  const onLast = (event) => {
    getMsgs(plast);
  }

  useEffect(() => {
    getUser();
    getMsgs(1);
  }, []);

  return (
    <div className="App">
      <h1 className="display-4 text-primary">SNS</h1>
      <p className="fs-3">logined: "{user}"/</p>
      <div>
        {message != '' &&
          <div className="alert alert-primary alert-dismissible fade show" role="alert">
            <p>{message}</p>
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
          </div>
        }
        <div className="content">
          <textarea className="form-control" onChange={doChange} value={content}></textarea>
          <button className="btn btn-primary" onClick={doAction}>
            Post!
          </button>
          <hr />
          <table className="table mt-3">
            <tr><th>Message</th></tr>
            {msgs.map(obj => (
              <tr><td>
                <p className="fs-4 my-0">
                  {obj.fields.content}
                </p>
                <p className="my-0 text-end">
                  <span className="fs-5">
                    "{obj.fields.owner_name}"
                  </span>
                  <span className="fs-6">
                    ( {obj.fields.pub_date} )
                  </span>
                  <p className="mt-1 fs-6 text-end">
                    <span className="h6 text-primary">
                      good= {obj.fields.good_count}
                    </span>
                    <span className="float-right">
                      <span className="mx-2">
                        {console.log(obj.fields)}
                      </span>
                      <button className="py-0 px-1 btn btn-outline-primary" id={obj.pk} onClick={doGood}>
                        good!
                      </button>
                    </span>
                  </p>
                </p>
              </td></tr>
            ))}
          </table>
          <ul class="pagination justify-content-center">
            <li class="page-item">
              <a class="page-link" href="#" onClick={onFirst}>
                &laquo; first
              </a>
            </li>
            <li class="page-item">
              <a class="page-link" onClick={onPrev} href="#">
                &laquo; prev
              </a>
            </li>
            <li class="page-item">
              <a class="page-link">
                {pnum}{plast}
              </a>
            </li>
            <li class="page-item">
              <a class="page-link" onClick={onNext} href="#">
                next &raquo;
              </a>
            </li>
            <li class="page-item">
              <a class="page-link" onClick={onLast} href="#">
                last &raquo;
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default App;