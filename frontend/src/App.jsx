import {useState} from 'react';
import styles from './App.module.css';
import {en, Faker} from '@faker-js/faker';

// eslint-disable-next-line react-refresh/only-export-components
export const faker = new Faker({
  locale: [en],
});

const App = () => {
  const [posts, setPosts] = useState('');
  const [messages, setMessages] = useState([]);

  const addPost = () => {
    const randomName = faker.internet.userName();
    const uniqueId = faker.string.uuid(); // Generate a unique ID for each post

    if (posts.trim()) {
      setMessages([...messages, {id: uniqueId, name: randomName, message: posts}]);
      setPosts(''); // Clear the input after adding the post
    }
  };

  return (
    <div className={styles.container}>
      <p>Chat</p>
      <div className={styles.board}>
        <div className={styles.messages}>
          {messages.map((post) => (
            <p key={post.id}>
              <span>😁{post.name}</span> - {new Date().toLocaleString()}
              <br/>
              {post.message}
            </p>
          ))}
        </div>
        <div className={styles.input}>
          <textarea
            value={posts}
            onChange={(e) => setPosts(e.target.value)}
            placeholder="Enter your message"
            rows="4"
            cols="50"
          />
          <button onClick={addPost}>Add post</button>
        </div>
      </div>
    </div>
  );
};

export default App;
