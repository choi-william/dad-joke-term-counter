import React, {Component} from 'react'
import ReactDOM from 'react-dom';
import './index.css';
import Table from './Table';

const state = {
  data: []
};

export default class App extends Component {
  render() {
    const data = [
      {
        rank: 1,
        term: 'Janitor',
        count: 10
      },
      {
        rank: 1,
        term: 'Janitor',
        count: 10
      },
      {
        rank: 1,
        term: 'Janitor',
        count: 10
      }
    ];

    function handleClick() {
      fetch('http://localhost:5000/jokes',{
        mode: 'cors'
      })
        .then(result => result.json())
        .then(result => {
            setState({
            data: result.data
          })
        });
    }

    return(
      <div className="App">
        <h1>Dad Joke Term Counter</h1>
          <button className="Button" onClick={handleClick}>
            Get me counts!
          </button>
        <Table dadJokeData={state.data} />
      </div>
    );
  }
}

function setState(newState) {
  Object.assign(state, newState)
  renderApp()
}

function renderApp() {
  ReactDOM.render(<App />, document.getElementById('root'))
}