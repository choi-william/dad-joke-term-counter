import React, {Component} from 'react'
import './index.css';

function TableHeader() {
  return(
    <thead>
      <tr>
        <th>Rank</th>
        <th>Term</th>
        <th>Count</th>
      </tr>
    </thead>
  );
}

class Table extends Component {
  render() {
    const {dadJokeData} = this.props;
    const tableRows = dadJokeData.map((data, index) =>
      <tr>
        <td>{index+1}</td>
        <td>{data.term}</td>
        <td>{data.count}</td>
      </tr>
    );

    return (
      <table>
        <TableHeader />
        <tbody>
          {tableRows}
        </tbody>
      </table>
    );
  }
}